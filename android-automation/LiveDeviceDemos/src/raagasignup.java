import java.net.MalformedURLException;
import java.time.Duration;

import org.openqa.selenium.Dimension;

import io.appium.java_client.TouchAction;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

public class raagasignup extends base {

	public static void main(String[] args) throws MalformedURLException {
		// TODO Auto-generated method stub

		/*
		 * swipe splash screen 2x to see cards, select Done, select Sign Up
		 * fill full name, fill username, fill email, fill password, print out text above year of birth
		 * fill year of birth, fill gender, click Create
		 */
		AndroidDriver<AndroidElement> driver = Capabilities();
		TouchAction t = new TouchAction(driver);
		/* this code for swiping isn't working on the Raaga app, but working on Google Play Store app
		Dimension size = driver.manage().window().getSize();
		System.out.println(size);
		int startx = (int)(size.width * 0.70);
		int endx = (int)(size.width * 0.80);
		int starty = (int) (size.height / 1.3);
		t.press(startx, starty).waitAction(Duration.ofMillis(1000)).moveTo(endx, starty).release().perform();
		*/
		driver.findElementById("android:id/button2").click();
		t.tap(driver.findElementById("com.raaga.android:id/skip_text")).perform();		
		t.tap(driver.findElementById("com.raaga.android:id/landing_signup_btn")).perform();
		driver.findElementById("com.raaga.android:id/signup_name").sendKeys("John Smith");
		driver.findElementById("com.raaga.android:id/signup_user_name").sendKeys("jsmith86");
		driver.findElementById("com.raaga.android:id/signup_email").sendKeys("jsmith86@gmail.com");
		driver.findElementById("com.raaga.android:id/signup_password").sendKeys("Testing1234!");
		System.out.println(driver.findElementById("com.raaga.android:id/signup_need_btn").getText());
		t.tap(driver.findElementByAndroidUIAutomator("resourceId(\"com.raaga.android:id/signup_year\")")).perform();
		t.tap(driver.findElementByAndroidUIAutomator("resourceId(\"com.raaga.android:id/signup_year\")")).perform();
		
		t.press(1000, 3000).perform();
		t.press(1000, 3000).perform();
		t.press(1000, 3000).perform();
		
		
		driver.findElementById("com.raaga.android:id/year_minus").click();
		driver.findElementById("com.raaga.android:id/year_minus").click();
		driver.findElementById("com.raaga.android:id/year_minus").click();

		t.tap(driver.findElementById("com.raaga.android:id/year_minus")).perform();
		t.tap(driver.findElementById("com.raaga.android:id/year_minus")).perform();
			/*
		int x=1;
		for(x=1; x<=20; x++) {
			t.tap(driver.findElementById("com.raaga.android:id/year_minus")).perform();
		}
		*/
		t.tap(driver.findElementById("com.raaga.android:id/SetDateTime")).perform();
		t.tap(driver.findElementById("com.raaga.android:id/signup_gender")).perform();		
		t.tap(driver.findElementById("com.raaga.android:id/signup_gender")).perform();	
		t.tap(driver.findElementByAndroidUIAutomator("resourceId(\"com.raaga.android:id/custom_alert_male\")")).perform();
		t.tap(driver.findElementById("com.raaga.android:id/signup_submit_btn")).perform();
		
	}

}
