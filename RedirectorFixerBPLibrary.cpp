#include "RedirectorFixerBPLibrary.h"
#include "Developer/AssetTools/Public/AssetToolsModule.h"
#include "Developer/AssetTools/Public/IAssetTools.h"
#include "Runtime/CoreUObject/Public/UObject/ObjectRedirector.h"

void URedirectorFixerBPLibrary::FixupReferencers(const TArray<FString>& ObjectPaths)
{
    TArray<UObjectRedirector*> Redirectors;
    
    for (const FString& ObjectPath : ObjectPaths)
    {
        if (UObject* LoadedObject = LoadObject<UObject>(nullptr, *ObjectPath))
        {
            if (UObjectRedirector* Redirector = Cast<UObjectRedirector>(LoadedObject))
            {
                Redirectors.Add(Redirector);
            }
        }
    }

    if (Redirectors.Num() > 0)
    {
        FAssetToolsModule& AssetToolsModule = FModuleManager::LoadModuleChecked<FAssetToolsModule>(TEXT("AssetTools"));
        AssetToolsModule.Get().FixupReferencers(Redirectors);
    }
}


