import java.net.MalformedURLException;
import java.util.concurrent.TimeUnit;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

public class uiautomatortest extends base {

	public static void main(String[] args) throws MalformedURLException {
		// TODO Auto-generated method stub

		AndroidDriver<AndroidElement> driver = Capabilities();
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		
		//driver.findElementByAndroidUIAutomator("attribute(\"value\")").click();
		driver.findElementByAndroidUIAutomator("text(\"Views\")").click();
		
		//driver.findElementsByAndroidUIAutomator("new UiSelector().property(value)");
		//this will check and print out the number of properties on the screen that are clickable, in this case, zero
		System.out.println(driver.findElementsByAndroidUIAutomator("new UiSelector().clickable(true)"));
		
	}

}
