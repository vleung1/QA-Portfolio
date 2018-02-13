import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;
import io.appium.java_client.remote.MobileCapabilityType;
import io.appium.java_client.remote.MobilePlatform;

public class base {

	public static AndroidDriver<AndroidElement> Capabilities() throws MalformedURLException {
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
		cap.setCapability("appPackage", "com.raaga.android");
		//set activity name (app screen to load)
		cap.setCapability("appActivity", "com.raaga.android.SplashScreen");
		//set connection to appium
		AndroidDriver<AndroidElement> driver = new AndroidDriver<>(new URL("http://127.0.0.1:4723/wd/hub"), cap);
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		return driver;
		
		/*
		this is config for loading app onto device via the src folder similar to running on emulator
		File f = new File("src");
		File fs = new File(f, "Raaga.apk");
		DesiredCapabilities cap = new DesiredCapabilities();
		cap.setCapability(MobileCapabilityType.PLATFORM_NAME, MobilePlatform.ANDROID);
		cap.setCapability(MobileCapabilityType.DEVICE_NAME, "Android Device");
		cap.setCapability(MobileCapabilityType.NEW_COMMAND_TIMEOUT, "25");
		cap.setCapability(MobileCapabilityType.APP, fs.getAbsolutePath());
		AndroidDriver<AndroidElement> driver = new AndroidDriver<>(new URL("http://127.0.0.1:4723/wd/hub"), cap);
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		*/
	}

}
