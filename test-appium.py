from appium import webdriver as wd
from time import sleep
from thread import start_new_thread
from subprocess import call
from subprocess import check_output as co

desired_caps = {
    "platformName": "android",
    "appPackage": "com.ghostery.android.ghostery",
    "appActivity": "org.mozilla.gecko.LauncherActivity",
    "deviceName": "Nexus 5",
    "automationName": "UiAutomator2",
    "app": "http://repository.cliqz.com.s3.amazonaws.com/dist/android/nightly/ghostery/latest_x86.apk",
    "noReset" : True
}

def checkDevice():
	out = co(["adb", "devices"])
	print(out)
	if ("emulator" in out) or ("exus" in out):
		return True
	else:
		return False

if __name__ == "__main__":
	try:
		emulator = start_new_thread(call, (["$ANDROID_HOME/emulator/emulator", "-avd", "Nexus5Emu"],))
		total = 120
		count = 1
		while count < total:
			if checkDevice:
				break
			count += 1
		appium = start_new_thread(call, (["appium"],))
		driver = WD.Remote("http://localhost:4723/wd/hub", desired_caps)
		sleep(15)
		print(driver.page_source)
	except Exception as e:
		print(e)
	finally:
		driver.quit()
		appium.conjugate()
		emulator.conjugate()
