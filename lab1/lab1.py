
# coding: utf-8

# In[1]:


import ctypes
from ctypes import windll, byref, Structure, Array, wintypes

class SYSTEM_INFO(ctypes.Structure):
    _fields_ = [("GetPhysicallyInstalledSystemMemory", wintypes.ULONG)]
SystemInfo = SYSTEM_INFO()
SystemInfo.dwLength = ctypes.sizeof(SYSTEM_INFO)
ctypes.windll.kernel32.GetPhysicallyInstalledSystemMemory(ctypes.byref(SystemInfo))
print("%s: %s (0x%x)" % ("RAM", SystemInfo.GetPhysicallyInstalledSystemMemory, SystemInfo.GetPhysicallyInstalledSystemMemory))

