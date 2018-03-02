import java.net.MalformedURLException;
import java.time.Duration;
import java.util.HashMap;

import org.openqa.selenium.Dimension;
import org.openqa.selenium.JavascriptExecutor;

import io.appium.java_client.TouchAction;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class menuBrowse extends base{

	public static void main(String[] args) throws MalformedURLException {

		IOSDriver<IOSElement> driver = Capabilities();
		TouchAction t = new TouchAction(driver);
		t.tap(driver.findElementByAccessibilityId("Alert Views")).perform();
		t.tap(driver.findElementByXPath("//*[@value='Text Entry']")).perform();
		driver.findElementByClassName("XCUIElementTypeTextField").sendKeys("hello");
		//could not use touchaction tap here because it did not allow for navigate().back() in next step to work
		driver.findElementByName("OK").click();
		driver.navigate().back();
		
		Dimension size = driver.manage().window().getSize();
		System.out.println(size);
		int x = (int) (size.width / 2);
		int starty = (int)(size.height * 0.80);
		int endy = (int)(size.height * 0.10);
		t.press(x, starty).moveTo(x, endy).release().perform();

		//t.press(x,600).moveTo(x,150).release().perform();
		/*
		JavascriptExecutor js = (JavascriptExecutor) driver;

		HashMap scrollObject = new HashMap();

		scrollObject.put("direction", "down");aa

		js.executeScript("mobile: scroll", scrollObject);
		*/
		//t.tap(driver.findElementByAccessibilityId("Steppers")).perform();

	}

}
