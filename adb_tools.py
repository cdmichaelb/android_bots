# Various tools to interact with the Android Debug Bridge (adb)
import os

class AdbTools:
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        """
        Returns a string representation of the object
        """
        return 'AdbTools'

    def get_devices(self) -> list:
        """
        Returns a list of devices connected to the host
        """
        return self.run_adb_command('devices').split('\n')[1:]
    
    def get_screen_resolution(self, device_id) -> str:
        """
        Returns the screen resolution of the device
        """
        return self.run_adb_command('shell wm size', device_id)
    
    def set_screen_resolution(self, device_id, resolution) -> None:
        """
        Sets the screen resolution of the device
        """
        return self.run_adb_command('shell wm size ' + resolution, device_id)
    
    def take_screenshot(self, device_id, filename) -> None:
        """
        Takes a screenshot of the device and saves it to the specified file
        """
        return self.run_adb_command('exec-out screencap -p', device_id, filename)
    
    def pull_file(self, device_id, source, destination) -> None:
        """
        Pulls a file from the device with the specified ID
        """
        return self.run_adb_command('pull ' + source + ' ' + destination, device_id)
    
    def run_adb_command(self, command, device_id=None, filename=None) -> str:
        """
        Runs the specified command on the Android Debug Bridge (adb)
        """
        new_command = 'adb '
        if device_id is not None:
            new_command += '-s ' + device_id + ' '
            
        new_command += command
        
        if filename is not None:
            new_command += ' > ' + filename
        
        print(new_command)
        return os.popen(new_command).read()
    
    def get_device_id(self, device_name) -> str:
        """
        Returns the device ID of the device with the specified name
        """
        devices = self.get_devices()
        for device in devices:
            if device_name in device:
                return device.split('\t')[0]
        return None
    
    def get_device_name(self, device_id) -> str:
        """
        Returns the device name of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[1]
        return None
    
    def get_device_state(self, device_id) -> str:
        """
        Returns the state of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[2]
        return None
    
    def get_device_type(self, device_id) -> str:
        """
        Returns the type of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[3]
        return None
    
    def get_device_version(self, device_id) -> str:
        """
        Returns the version of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[4]
            
    def get_device_model(self, device_id) -> str:
        """
        Returns the model of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[5]
            
    def get_device_product(self, device_id) -> str:
        """
        Returns the product of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[6]
            
    def get_device_brand(self, device_id) -> str:
        """
        Returns the brand of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[7]
            
    def get_device_tags(self, device_id) -> list:
        """
        Returns the tags of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[8]
            
    def get_device_sdk_version(self, device_id) -> str:
        """
        Returns the SDK version of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[9]
            
    def get_device_screen_density(self, device_id) -> str:
        """
        Returns the screen density of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[10]
            
    def get_device_screen_size(self, device_id) -> tuple:
        """
        Returns the screen size of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[11]
            
    def get_device_screen_orientation(self, device_id) -> str:
        """
        Returns the screen orientation of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[12]
            
    def get_device_locale(self, device_id) -> str:
        """
        Returns the locale of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[13]
            
    def get_device_time(self, device_id) -> str:
        """
        Returns the time of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[14]
            
    def get_device_country(self, device_id) -> str:
        """
        Returns the country of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[15]
            
    def get_device_language(self, device_id) -> str:
        """
        Returns the language of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[16]
            
    def get_device_build_id(self, device_id) -> str:    
        """
        Returns the build ID of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[17]
            
    def get_device_build_version_release(self, device_id) -> str:
        """
        Returns the build version release of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[18]
            
    def get_device_build_version_sdk(self, device_id) -> str:
        """
        Returns the build version SDK of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[19]
            
    def get_device_build_version_incremental(self, device_id) -> str:
        """
        Returns the build version incremental of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[20]
            
    def get_device_build_type(self, device_id) -> str:
        """
        Returns the build type of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[21]
            
    def get_device_build_tags(self, device_id) -> str:
        """
        Returns the build tags of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[22]
            
    def get_device_build_flavor(self, device_id) -> str:
        """
        Returns the build flavor of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[23]
            
    def get_device_build_fingerprint(self, device_id) -> str:
        """
        Returns the build fingerprint of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[24]
            
    def get_device_build_user(self, device_id) -> str:
        """
        Returns the build user of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[25]
            
    def get_device_build_host(self, device_id) -> str:
        """
        Returns the build host of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[26]
    
    def get_device_build_id(self, device_id) -> str:
        """
        Returns the build id of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[27]
            
    def get_device_build_date(self, device_id) -> str:
        """
        Returns the build date of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[28]
            
    def get_device_build_time(self, device_id) -> str:
        """
        Returns the build time of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[29]
            
    def get_device_build_codename(self, device_id) -> str:
        """
        Returns the build codename of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[30]
            
    def get_device_build_bootloader(self, device_id) -> str:
        """
        Returns the build bootloader of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[31]
            
    def get_device_build_hardware(self, device_id) -> str:
        """
        Returns the build hardware of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                return device.split('\t')[32]
            
    def set_device_rotation(self, device_id, rotation) -> None:
        """
        Sets the rotation of the device with the specified ID
        """
        devices = self.get_devices()
        for device in devices:
            if device_id in device:
                device_info = device.split('\t')
                device_info[33] = rotation
                device = '\t'.join(device_info)
                self.set_devices(devices)
                return True
        return False
    
    def adb_launch_activity(self, device_id, package, activity) -> None:
        """
        Launches the specified activity on the device with the specified ID
        """
        return self.adb_shell('am start -n %s/%s' % (package, activity), device_id)
    
    def adb_close_activity(self, device_id, package, activity) -> None:
        """
        Closes the specified activity on the device with the specified ID
        """
        return self.adb_shell('am force-stop %s' % package, device_id)
    
    def adb_list_packages(self, device_id) -> list:
        """
        Returns a list of installed packages on the device with the specified ID
        """
        return self.adb_shell('pm list packages', device_id)
    
    def adb_list_activities(self, device_id, package) -> list:
        """
        Returns a list of activities in the specified package on the device with the specified ID
        """
        return self.adb_shell('pm list packages -a', device_id)
    
    def adb_install_apk(self, device_id, apk_path) -> None:
        """
        Installs the specified APK on the device with the specified ID
        """
        return self.adb_shell('pm install -r %s' % apk_path, device_id)
    
    def adb_uninstall_apk(self, device_id, package) -> None:
        """
        Uninstalls the specified package on the device with the specified ID
        """
        return self.adb_shell('pm uninstall %s' % package, device_id)
    
    def adb_clear_app_data(self, device_id, package) -> None:
        """
        Clears the app data of the specified package on the device with the specified ID
        """
        return self.adb_shell('pm clear %s' % package, device_id)
    
    def adb_clear_app_cache(self, device_id, package) -> None:
        """
        Clears the app cache of the specified package on the device with the specified ID
        """
        return self.adb_shell('pm clear %s' % package, device_id)
    
    def adb_clear_app_user_data(self, device_id, package) -> None:
        """
        Clears the app user data of the specified package on the device with the specified ID
        """
        return self.adb_shell('pm clear %s' % package, device_id)

    def adb_clear_app_user_data_by_id(self, device_id, package_id) -> None:
        """
        Clears the app user data of the specified package on the device with the specified ID
        """
        return self.adb_shell('pm clear %s' % package_id, device_id)
    
    def adb_clear_app_user_data_by_name(self, device_id, package_name) -> None:
        """
        Clears the app user data of the specified package on the device with the specified ID
        """
        return self.adb_shell('pm clear %s' % package_name, device_id)
    
    def adb_clear_app_user_data_by_package_name(self, device_id, package_name) -> None:
        """
        Clears the app user data of the specified package on the device with the specified ID
        """
        return self.adb_shell('pm clear %s' % package_name, device_id)
    
    def adb_connect_emulator(self, device_id) -> None:
        """
        Connects to the specified emulator
        """
        return self.adb_connect('emulator-%s' % device_id)
    
    def adb_connect(self, device_id, device_port=None) -> None:
        """
        Connects to the specified device
        """
        return self.run_adb_command(f'connect {device_id}:{device_port}')

if __name__ == '__main__':
    
    import time
    adb = AdbTools()
    print(adb.get_devices())
    device = '5575'
    adb.adb_connect('localhost', device)
    while True:
        # wait 3 seconds
        time.sleep(.25)
        
        adb.take_screenshot(f'localhost:{device}', 'screenshot.png')
