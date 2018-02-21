import java.net.MalformedURLException;

import org.openqa.selenium.JavascriptExecutor;

import io.appium.java_client.TouchAction;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

public class browserTest extends baseChrome {

	public static void main(String[] args) throws MalformedURLException {

		AndroidDriver<AndroidElement> driver = Capabilities();
		TouchAction t = new TouchAction(driver);
		
		/* facebook test
		driver.get("http://www.facebook.com");
		driver.findElementByXPath("//*[@id='m_login_email']").sendKeys("qwwerty");
		driver.findElementByName("pass").sendKeys("123456");
		driver.findElementByXPath("//button[@name='login']").click();
		*/
		/* cricbuzz test
		driver.get("http://cricbuzz.com");
		driver.findElementByXPath("//a[@href='#menu']").click();
		driver.findElementByCssSelector("a[title='Cricbuzz Home']").click();
		System.out.println(driver.getCurrentUrl());
		JavascriptExecutor jse = (JavascriptExecutor) driver;
		jse.executeScript("window.scrollBy(0,480)", "");
		Assert.assertTrue(driver.findElementByXPath("//h4[@text()='Top Stories']").getAttribute("class").contains("header"));
		*/
		
		//go to ebay on mobile browser, search for books, and output first 2 listings
		driver.get("http://ebay.com");
		driver.findElementByXPath("//input[@type='search']").sendKeys("books");
		driver.findElementByXPath("//input[@type='submit']").click();
		System.out.println(driver.findElementsByClassName("s-item__title").get(0).getAttribute("textContent"));
		System.out.println(driver.findElementsByClassName("s-item__title").get(1).getAttribute("textContent"));


	}

}
