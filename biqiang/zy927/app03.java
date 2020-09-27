import java.net.MalformedURLException;
import java.net.URL;

import io.appium.java_client.AppiumDriver;

import org.openqa.selenium.remote.DesiredCapabilities;


public class app03 {

	public static void main(String[] args) throws MalformedURLException {
		// TODO Auto-generated method stub
		//创建DesiredCapabilities的对象
				DesiredCapabilities des = new DesiredCapabilities();
				//des的方法setCapability（）设置键值对
				des.setCapability("platformName", "Android");
				des.setCapability("deviceName", "Android Emulator");
				des.setCapability("platformVersion", "4.4.4");
				//再添加一个键值对，不让app每次测试都重置一遍
				des.setCapability("noReset", true);
				des.setCapability("appPackage", "com.android2.calculator3");
				des.setCapability("appActivity","com.android2.calculator3.Calculator");
				
				//创建Appium的对象
				AppiumDriver driver = new AppiumDriver(new URL("http://127.0.0.1:4723/wd/hub"),des);
			
				//定位到计算器的按键1，并点击
				driver.findElementById("com.android2.calculator3:id/digit_1").click();

				//点击+
				driver.findElementById("com.android2.calculator3:id/op_add").click();
				//点击2
				driver.findElementById("com.android2.calculator3:id/digit_2").click();
				//点等号
				driver.findElementById("com.android2.calculator3:id/eq").click();
				//定义预期结果变量
				String expectValue = "3";
				//获取实际结果，使用getAttribute("text")
				String acutalValue = driver.findElementById("com.android2.calculator3:id/formula").getAttribute("text");
				
				//判断是否相等
				if(expectValue.equals(acutalValue)){
					System.out.println("加法运算实现是对的");
				}else{
					System.out.println("加法运算实现是错误的");
				}
	}

}
