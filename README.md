# Batch Fixup Redirector in Unreal
A very simple plugin and a python script to fix up redirector in batch in Unreal Engine without the engine crashing up.

## How to use
1. In your poject folder put the plugin folder in the folder called Plugins (Create the Plugins folder if it does not exist) </br></br> ![image](https://github.com/user-attachments/assets/c531554b-cced-4bb1-929e-f8c0a34531f0) </br>

2. When you open your .uproject it will ask to compile the project (make sure you have VS set up properly)<br/>
3. Run the python file from output log as shown in the image, make sure to set it to python from cmd </br></br>
![image](https://github.com/user-attachments/assets/04706f52-b86f-46ca-9668-0d7880e94e3d)

## Edit the python file to suit your need

![image](https://github.com/user-attachments/assets/d2058fdb-1c65-4f22-ae7c-02d642d1e3d1)
</br>
<br/>

1.You can keep the fixup.py anywhere and run it from there.<br/>
2. Change the path shown in the **fixup.py** from here.<br/>
3. The path will fix up all redirectors inside that folder, including sub folder.<br/>
4. Make sure the path starts with /Game/ and is the path from inside the engine, not your windows directory.<br/>
5. Unless you have all assets loaded in cache, avoid running the script from /Game/ it will cause the engine to load up all assets, and that may take CPU resources and time.<br/>
