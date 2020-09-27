import java.net.MalformedURLException;
import java.net.URL;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.TouchAction;
import org.openqa.selenium.remote.DesiredCapabilities;


public class app02 {

	public static void main(String[] args) throws MalformedURLException,InterruptedException {
		// TODO Auto-generated method stub
		//com.android.browser
		//com.android.browser:id/tab_switcher
		DesiredCapabilities des =new DesiredCapabilities();
		des.setCapability("platformName","android");
		des.setCapability("deviceName","Android Emulator");
		des.setCapability("platformVersion","4.4.4");
		des.setCapability("noReset",true);
		des.setCapability("appPackage","com.tencent.mobileqq");
		des.setCapability("appActivity","com.tencent.mobileqq.activity.LoginActivity");
		//com.android.browser,com.android.browser.BrowserActivity
		AppiumDriver dr=new AppiumDriver(new URL("http://127.0.0.1:4723/wd/hub"),des);
		
		TouchAction touchAction = new TouchAction(dr);
		Thread.sleep(3000);
//请输入QQ号码或手机或邮箱
		String[] str=new String[1];
		str[0]="107143";
		dr.findElementByAccessibilityId("请输入QQ号码或手机或邮箱").clear();
		dr.findElementByAccessibilityId("请输入QQ号码或手机或邮箱").sendKeys(str);
		
		String[] str2=new String[1];
		str2[0]="Joseph5";
//		//com.tencent.mobileqq:id/password
		
		dr.findElementById("com.tencent.mobileqq:id/password").click();
		dr.findElementById("com.tencent.mobileqq:id/password").sendKeys(str2);
		
//		
//		//com.tencent.mobileqq:id/login
		dr.findElementById("com.tencent.mobileqq:id/login").click();
		Thread.sleep(3000);
		
		dr.quit();
		
	}
}