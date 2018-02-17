import java.net.MalformedURLException;
import java.time.Duration;
import java.util.UUID;

import org.openqa.selenium.Dimension;

import io.appium.java_client.TouchAction;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

public class install extends base {

	public static void main(String[] args) throws MalformedURLException {

		AndroidDriver<AndroidElement> driver = Capabilities();
		TouchAction t = new TouchAction(driver);
		Dimension size = driver.manage().window().getSize();
		System.out.println(size);
		int starty = (int)(size.height * 0.50);
		int endy = (int)(size.height * 0.05);
		int startx = (int) (size.width / 2);
		
		t.tap(driver.findElementById("com.voicefive.mymobilesecure:id/beginButton")).perform();
		t.tap(driver.findElementByXPath("//*[@text='Allow']")).perform();
		t.tap(driver.findElementByXPath("//android.widget.Button[@text='I Agree']")).perform();
		driver.findElementsByClassName("android.widget.EditText").get(0).sendKeys("email" + generateString() + "@email.com");
		t.tap(driver.findElementsByClassName("android.widget.Spinner").get(0)).perform();
		driver.findElementByAndroidUIAutomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"18\"));");
		t.tap(driver.findElementByXPath("//android.widget.CheckedTextView[@text='18']")).perform();
		t.tap(driver.findElementsByClassName("android.widget.Spinner").get(1)).perform();
		t.tap(driver.findElementByXPath("//android.widget.CheckedTextView[@text='Female']")).perform();
		t.tap(driver.findElementsByClassName("android.widget.Spinner").get(2)).perform();
		driver.findElementByAndroidUIAutomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"$250,000 or more\"));");
		t.tap(driver.findElementByXPath("//android.widget.CheckedTextView[@text='$250,000 or more']")).perform();
		driver.findElementsByClassName("android.widget.EditText").get(1).sendKeys("11111");
		driver.hideKeyboard();
		driver.findElementByAndroidUIAutomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"HOUSEHOLD SIZE *\"));");
		t.tap(driver.findElementsByClassName("android.widget.Spinner").get(3)).perform();
		t.tap(driver.findElementByXPath("//android.widget.CheckedTextView[@text='5']")).perform();
		driver.findElementByAndroidUIAutomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"CHILDREN UNDER 18 IN HOME? *\"));");
		t.tap(driver.findElementsByClassName("android.widget.Spinner").get(4)).perform();
		t.tap(driver.findElementByXPath("//android.widget.CheckedTextView[@text='Yes']")).perform();
		driver.findElementByAndroidUIAutomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"RACE *\"));");
		t.tap(driver.findElementsByClassName("android.widget.Spinner").get(5)).perform();
		t.tap(driver.findElementByXPath("//android.widget.CheckedTextView[@text='Asian/Pacific Islander']")).perform();
		//Without this line, the vertical swipe fails. My guess is that by locating an element, it focuses back on the screen again correctly after the previous step of choosing from the dropdown choices
		driver.findElementByXPath("//android.view.View[@text='ZIP CODE *']");
		t.press(startx, starty).waitAction(Duration.ofMillis(1000)).moveTo(startx, endy).release().perform();
		t.tap(driver.findElementsByClassName("android.widget.Spinner").get(6)).perform();
		t.tap(driver.findElementByXPath("//android.widget.CheckedTextView[@text='not Spanish, Hispanic, or Latino']")).perform();
		t.tap(driver.findElementsByClassName("android.widget.Spinner").get(7)).perform();
		t.tap(driver.findElementByXPath("//android.widget.CheckedTextView[@text='English all or most of the time']")).perform();
		t.tap(driver.findElementsByClassName("android.widget.Spinner").get(8)).perform();
		t.tap(driver.findElementByXPath("//android.widget.CheckedTextView[@text='English']")).perform();
		//t.tap(driver.findElementById("submit")).perform();

		
		/* accessibility settings steps
		t.tap(driver.findElementByXPath("//android.widget.TextView[@text='MyMobileSecure']")).perform();
		t.tap(driver.findElementById("com.android.settings:id/switch_widget")).perform();
		t.tap(driver.findElementByXPath("//*[@text='OK']")).perform();
		t.tap(driver.findElementById("com.android.settings:id/switch_widget")).perform();
		t.tap(driver.findElementByXPath("//*[@text='OK']")).perform();
		*/
	}
	
	public static String generateString() {
        String uuid = UUID.randomUUID().toString().replaceAll("-", "");
        System.out.println("uuid = " + uuid);
		return uuid;
    }

}
