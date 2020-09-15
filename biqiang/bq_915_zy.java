package joe_prac;

import java.util.Scanner;

public class bq_915_zy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		1．While（）里可以填数字吗？
//		不可以
//		2．外循环2次内循环4次，那么一共循环了多少次
//		8次
//		3．Break可以一次跳出2个循环吗？
//		不可以
//		4．数组是什么，他在作用是什么？
//		java内置的数据类型，线性的序列，长度固定，容量不变，会有边界检查；
//		一次性输入多个数据到函数。
//		5．请定义出一个可以储存8个整型的数组
//		int[] a1= new int[8];
//		6．编程题：数组元素查找(查找指定元素第一次在数组中出现的索引)
		Scanner scanner=new Scanner(System.in);
//		int a1[]= {1,2,3,4,5,6,7,8,9};
//		System.out.println("输入要找的数字：");
//		int b1=scanner.nextInt();
//		
//		for(int i=0;i<a1.length;i++) {
//			if(a1[i]==b1) {
//				System.out.println("索引为"+i);
//			}
//		}
//		案例:小芳的妈妈每天给她2.5元钱，她都会存起来，但是，每当这一天是存钱的第5天或者5的倍数的话，
//		她都会花去6元钱，请问，经过多少天，小芳才可以存到100元钱。
//		float u=2.5f;
//		int i;//day
//		for(i=1 ;u<100;i++) {
//			u+=2.5;
//			if(i%5==0) {
//				u-=6;
//			}
//		}
//		System.out.println(i);
//		
//		int day=0;
//		float money=0;
//		
//		while(money<100) {
//			money+=2.5;
//			day+=1;
//			if(day%5==0) {
//				money-=6;
//			}
//		}
//		System.out.println(day);
		
//		案例:输出1-100的单数
		int a2=0;
		do {
			if(a2%2==1) {
				System.out.println(a2);
			}
			a2+=1;
		}while(a2<=100);
		
//		案例:使用while嵌套循环打印如下图形
//		*
//		* *
//		* * *
//		* * * *
//		* * * * *
		int i3=0;
		while(i3<5) {
			int u3=0;
			while(u3<=i3) {
				System.out.print('*');
				u3++;
			}
			i3++;
			System.out.println();
		}
		
//		案例:输入一个整数,然后打印0到这个整数,最后打印0到这个整数之和
//		System.out.println("输入一个整数：");
//		int a4=scanner.nextInt(),b4=0;
//		for(int i4=0;i4<=a4;i4++) {
//			System.out.println(i4);
//			b4+=i4;
//		}
//		System.out.println(b4);
		
//		案例:n的阶乘，从外部键盘输入一个数字n
//		System.out.println("输入一个整数：");
//		int a5=scanner.nextInt(),b5=1;
//		for(int i=1;i<=a5;i++) {
//			b5*=i;
//		}
//		System.out.println(b5);

//		案例:九九乘法口诀表
		
//		for(int i=1;i<=9;i++) {
//			for(int u=1;u<=i;u++) {
//				System.out.print(i+"*"+u+'='+u*i+"\t");
//			}
//			System.out.println();
//		}
		
//		打印0-9的数字,不要打印出5来
		for(int i=0;i<=9;i++) {
			if(i==5) {
				continue;
			}
			System.out.println(i);
			
		}
		
//		案例:定义一个整型数数组,然后赋予数据,然后逆序打印
		int[] sz1=new int[10];
		for(int i=0;i<=9;i++) {
			sz1[i]=(int)(Math.random()*100);
		}
		for(int i:sz1) {
			System.out.print(i+" ");
		}
		System.out.println();
		for(int i=0,temp;i<sz1.length/2;i++) {
			temp=sz1[i];
			sz1[i]=sz1[sz1.length-1-i];
			sz1[sz1.length-1-i]=temp;
		}
		for(int i:sz1) {
			System.out.print(i+" ");
		}
		System.out.println();
		System.out.println("--------------------");
		
//		案例:求一维数组的最值
		int[] sz2=new int[10];
		for(int i=0;i<=9;i++) {
			sz2[i]=(int)(Math.random()*100);
		}
		for(int i:sz2) {
			System.out.print(i+" ");
			
		}
		System.out.println();
		int max=sz2[0],min=sz2[0];
		for(int i:sz2) {
			if(max<i) {
				max=i;
			}
			if(min>i) {
				min=i;
			}
			
			
		}
		System.out.println("最大值是"+max+"最小值是"+min);
		
//		案例:从控制台输入字符串,然后把字符串中的字符存储到字符数组中,然后打印出来
		System.out.println("输入字符串:");
		String a7=scanner.next();
		char[] b7=new char[a7.length()];
		for(int i=0;i<a7.length();i++) {
			b7[i]=a7.charAt(i);
		}
		for(int i=0;i<b7.length;i++) {
			System.out.println(b7[i]);
		}
		
		
		
	}

}
