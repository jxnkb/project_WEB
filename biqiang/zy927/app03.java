import java.net.MalformedURLException;
import java.net.URL;

import io.appium.java_client.AppiumDriver;

import org.openqa.selenium.remote.DesiredCapabilities;


public class app03 {

	public static void main(String[] args) throws MalformedURLException {
		// TODO Auto-generated method stub
		//����DesiredCapabilities�Ķ���
				DesiredCapabilities des = new DesiredCapabilities();
				//des�ķ���setCapability�������ü�ֵ��
				des.setCapability("platformName", "Android");
				des.setCapability("deviceName", "Android Emulator");
				des.setCapability("platformVersion", "4.4.4");
				//�����һ����ֵ�ԣ�����appÿ�β��Զ�����һ��
				des.setCapability("noReset", true);
				des.setCapability("appPackage", "com.android2.calculator3");
				des.setCapability("appActivity","com.android2.calculator3.Calculator");
				
				//����Appium�Ķ���
				AppiumDriver driver = new AppiumDriver(new URL("http://127.0.0.1:4723/wd/hub"),des);
			
				//��λ���������İ���1�������
				driver.findElementById("com.android2.calculator3:id/digit_1").click();

				//���+
				driver.findElementById("com.android2.calculator3:id/op_add").click();
				//���2
				driver.findElementById("com.android2.calculator3:id/digit_2").click();
				//��Ⱥ�
				driver.findElementById("com.android2.calculator3:id/eq").click();
				//����Ԥ�ڽ������
				String expectValue = "3";
				//��ȡʵ�ʽ����ʹ��getAttribute("text")
				String acutalValue = driver.findElementById("com.android2.calculator3:id/formula").getAttribute("text");
				
				//�ж��Ƿ����
				if(expectValue.equals(acutalValue)){
					System.out.println("�ӷ�����ʵ���ǶԵ�");
				}else{
					System.out.println("�ӷ�����ʵ���Ǵ����");
				}
	}

}
