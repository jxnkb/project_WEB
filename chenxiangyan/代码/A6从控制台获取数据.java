package test3;
import java.util.Scanner;
public class A6从控制台获取数据 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
        //生成一个对象
		Scanner scan=new Scanner(System.in);
		int i=scan.nextInt();
		System.out.println(i);
		float f=scan.nextFloat();
		float f1=20.22f;
		System.out.println(f);
		String string=scan.next();
		System.out.println(string);
        String string1=scan.next();//不管回车
        System.out.println(string1);
        String string2=scan.nextLine();//回车会被收入
        System.out.println(string2);
        System.out.println("函数结束");
        
	}

}
