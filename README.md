# Batch Fixup Redirector in Unreal
A very simple plugin and a python script to fix up redirector in batch in Unreal Engine without the engine crashing up.

## How to use
1. In your poject folder put the plugin folder in the folder called Plugins (Create the Plugins folder if it does not exist) </br></br> ![image](https://github.com/user-attachments/assets/c531554b-cced-4bb1-929e-f8c0a34531f0) </br>

2. When you open your .uproject it will ask to compile the project (make sure you have VS set up properly)<br/><br/>
3. Once the plugin is loaded you can run it from the uasset fie (blueprint widget) as shown below. All you have to do is copy the uasset file to your content folder, right click in enginge and select run widget.<br/><br/>
![image](https://github.com/user-attachments/assets/1e34a62f-86a5-44d9-87b9-e965796dd244)

4. Or it can be run as a python file from output log as shown in the image, make sure to set it to python from cmd </br></br>
![image](https://github.com/user-attachments/assets/04706f52-b86f-46ca-9668-0d7880e94e3d)

### Running using the fixup.py instead of the blueprint widget

![image](https://github.com/user-attachments/assets/d2058fdb-1c65-4f22-ae7c-02d642d1e3d1)
</br>
<br/>

1.You can keep the fixup.py anywhere and run it from there.<br/><br/>
2. Change the path shown in the **fixup.py** from here.<br/><br/>
3. The path will fix up all redirectors inside that folder, including sub folder.<br/><br/>
4. Make sure the path starts with /Game/ and is the path from inside the engine, not your windows directory.<br/><br/>
5. Unless you have all assets loaded in cache, avoid running the script from /Game/ it will cause the engine to load up all assets, and that may take CPU resources and time.<br/><br/>
