package maker2代码重敲;
import java.util.Random;

public class A06随机数 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		//方式一
		for(int i=0;i<10;i++) {
			int a=(int)(Math.random()*100);
			System.out.println(a);
		}
		
		//方式二
		Random r=new Random();
		for(int i=0;i<10;i++) {
			int a=r.nextInt(100);
			System.out.print(a+" ");
		}
		System.out.println("----------");
		
		//Math数学类
		System.out.println(Math.pow(3, 2)); //平方
		System.out.println(Math.sqrt(9));  //开根号
		System.out.println(Math.abs(-3));  //绝对值
		

	}

}
