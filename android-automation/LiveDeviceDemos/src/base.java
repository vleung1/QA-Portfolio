import java.net.MalformedURLException;
import java.net.URL;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;
import io.appium.java_client.remote.MobileCapabilityType;
import io.appium.java_client.remote.MobilePlatform;

public class base {

	public static void main(String[] args) throws MalformedURLException {
		// TODO Auto-generated method stub

		//this is for loading apps pre-installed on a real device
		DesiredCapabilities cap = new DesiredCapabilities();
		//set platform name
		cap.setCapability(MobileCapabilityType.PLATFORM_NAME, MobilePlatform.ANDROID);
		//set device name
		cap.setCapability(MobileCapabilityType.DEVICE_NAME, "Android Device");
		//set command timeout
		cap.setCapability(MobileCapabilityType.NEW_COMMAND_TIMEOUT, "25");
		//set package name
		cap.setCapability("appPackage", "com.tabtale.rowyourboat");
		//set activity name (app screen to load)
		cap.setCapability("appActivity", "com.tabtale.mpandroid.MainActivity");
		//set connection to appium
		AndroidDriver<AndroidElement> driver = new AndroidDriver<>(new URL("http://127.0.0.1:4723/wd/hub"), cap);
	}

}
