# device-watcher
select a device on your home wifi network and track its online/offline state.
## installation
1. install deps:
```bash
python -m pip install zeroconf
```
2. download device-watcher
3. you're done 
## usage
1. run device-watcher
2. turn on/wake up/unlock your device
3. wait for the spinner to finish spinning
4. sleep/close/lock your device
5. it should have found your device, and it should display it's mDNS name and it's IP address for your network
6. mess around with the device, locking/unlocking it and watch the current status change!
if you're device doesnt seem to work, open an issue and i'll add it to the list of unsupported devices
## confirmed supported devices
 - any Android device that supports nearby sharing and is on the latest version
## possibly supported?
 - iPhone/iPad
 - windows computer
 - linux computer
