import unreal
import time

def fix_redirectors(game_path, batch_size=1, delay_between_batches=2.0, delay_between_items=0.5):
    """
    Fix redirectors in the specified game path and its subfolders.
    
    Args:
        game_path (str): Path in the format '/Game/DLC/Avatars'
        batch_size (int): Number of redirectors to process in each batch
        delay_between_batches (float): Delay in seconds between processing batches
        delay_between_items (float): Delay in seconds between processing individual items
    """
    # Validate path format
    if not game_path.startswith("/Game/"):
        unreal.log_warning(f"Error: Path must start with '/Game/', received: {game_path}")
        return
        
    unreal.log(f"Processing redirectors in: {game_path}")
    unreal.log(f"Using batch size of {batch_size} with {delay_between_batches}s delay between batches")
    
    # Find all redirectors (loading with unloaded assets will cause you a world of pain, or mild inconvenience depending on pc, choose only the root folder of the redirectors, not /Game/
    redirectors = []
    asset_list = unreal.EditorAssetLibrary.list_assets(game_path, recursive=True, include_folder=True)
    
    processed_count = 0
    
    # Find all redirectors in the path
    for path in asset_list:
        # Add small delay every 50 items during search to prevent engine strain
        if processed_count > 0 and processed_count % 50 == 0:
            time.sleep(0.2)
            
        # Skip directories
        if unreal.EditorAssetLibrary.does_directory_exist(path):
            continue
            
        # Check if asset exists
        if unreal.EditorAssetLibrary.does_asset_exist(path):
            asset_data = unreal.EditorAssetLibrary.find_asset_data(path)
            asset_class = str(asset_data.asset_class)
            
            if asset_class == 'ObjectRedirector':
                # Remove the .asset_name part if present
                clean_path = path.split(".")[0]
                redirectors.append(clean_path)
                processed_count += 1
                unreal.log(f"Found redirector {processed_count}: {clean_path}")
    
    if not redirectors:
        unreal.log(f"No redirectors found in path: {game_path}")
        return
    
    total_redirectors = len(redirectors)
    unreal.log(f"\nFound {total_redirectors} redirectors to process...")
    
    # Process redirectors in batches
    for batch_start in range(0, total_redirectors, batch_size):
        batch_end = min(batch_start + batch_size, total_redirectors)
        current_batch = redirectors[batch_start:batch_end]
        batch_number = (batch_start // batch_size) + 1
        total_batches = (total_redirectors + batch_size - 1) // batch_size
        
        unreal.log(f"\nProcessing batch {batch_number}/{total_batches} ({len(current_batch)} redirectors)...")
        
        try:
            # Fix redirectors in this batch
            unreal.RedirectorFixerBPLibrary.fixup_referencers(current_batch)
            unreal.log(f"Successfully processed batch {batch_number}")
            
            # Save after each batch
            unreal.log("Saving changes for this batch...")
            unreal.EditorAssetLibrary.save_directory(game_path, recursive=True, only_if_is_dirty=False)
            
            # Force garbage collection after each batch
            unreal.SystemLibrary.collect_garbage()
            
            # Add delay between items in batch
            for i in range(len(current_batch)):
                if i > 0:  # Don't delay after the last item
                    time.sleep(delay_between_items)
            
            # Add delay between batches if not the last batch
            if batch_end < total_redirectors:
                unreal.log(f"Waiting {delay_between_batches}s before next batch...")
                time.sleep(delay_between_batches)
                
        except Exception as e:
            unreal.log_error(f"Error processing batch {batch_number}: {str(e)}")
            unreal.log_warning("Waiting additional time before continuing...")
            time.sleep(delay_between_batches * 2)  # Double delay after error
    
    # Final garbage collection
    unreal.SystemLibrary.collect_garbage()
    
    # Final log
    unreal.log("\nRedirector Fix Summary:")
    unreal.log(f"Total Redirectors Found and Processed: {total_redirectors}")
    unreal.log(f"Total Batches Processed: {total_batches}")
    unreal.log(f"Path Processed: {game_path}")
    unreal.log("\nProcess completed!")


############-----------------------------------###################
# ############## replace the path with your desired path #################################

GAME_PATH = "/Game/DLC/Avatars/Modular/"

# ######### CUSTOMISE THESE ############
fix_redirectors(
    game_path=GAME_PATH,
    batch_size=1,           # Process 5 redirectors at a time
    delay_between_batches=2.0,  # Wait 2 seconds between batches
    delay_between_items=5     # Wait 0.5 seconds between individual items
)
