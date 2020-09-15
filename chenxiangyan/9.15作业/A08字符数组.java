package maker2;

import java.util.Scanner;

public class A08字符数组 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		int[] arr=new int[5];
		for(int i=0;i<5;i++) {
			arr[i]=i;
		}
		System.out.println(arr);
		
		char[] myarr=new char[5];
		for(int i=0;i<5;i++) {
			myarr[i]='a';
		}
		
		System.out.println(myarr);//1.字符数组可以直接打印.
		
		String string="abcde";
		System.out.println(string);
		for(int i=0;i<string.length();i++) {//2.字符串.length()可以获取字符串的长度
			System.out.println(string.charAt(i));// 3.string.charAt(i)获取字符串中某个字符
		}
//		for(char i:string) {//报错
//			
//		}
		
//		案例:从控制台输入字符串,然后把字符串中的字符存储到字符数组中,然后打印出来
//		1.str.charAt(i);可以返回字符串中的字符,str是字符串
//		2.str.length();可以返回字符串的长度,str是字符串
		Scanner scanner=new Scanner(System.in);
		//从控制台获取字符串
		String str=scanner.next();
		//定义字符数组
		char[] mych=new char[str.length()];
		//给数组赋值
		for(int i=0;i<mych.length;i++) {//abcd
			mych[i]=str.charAt(i);
		}
		//注意:数组在等号的左边表示等待接收数值
		mych[0]='a';
		//数组在等号的右边表示从数组取值
		char c=mych[0];
		
		
		System.out.println(mych);
		
		
	}

}
