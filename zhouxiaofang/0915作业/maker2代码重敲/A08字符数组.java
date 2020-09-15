package maker2代码重敲;

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
		//1.字符数组可以直接打印
		System.out.println(myarr);
		
		String str="abcde";
		System.out.println(str);
		for(int i=0;i<str.length();i++) {//2.字符串.length()可以获取字符串的长度
			System.out.println(str.charAt(i));// 3.string.charAt(i)获取字符串中某个字符
		}
		
	//	for(char i:str) { //报错
			
	//	}
		
//		案例:从控制台输入字符串,然后把字符串中的字符存储到字符数组中,然后打印出来
//		1.str.charAt(i);可以返回字符串中的字符,str是字符串
//		2.str.length();可以返回字符串的长度,str是字符串
		
		Scanner str1=new Scanner(System.in);
		//从控制台获取字符串
		String mystr=str1.next();
		//定义字符数组
		char[] mych=new char[mystr.length()];
		//给数组赋值
		for(int i=0;i<mych.length;i++) {
			mych[i]=mystr.charAt(i);
		}
		//注意:数组在等号的左边表示等待接受数值
		mych[0]='a';
		//数组在等号的右边表示从数组取值
		char c=mych[0];
		
		System.out.println(mych);
		
	
		
		
		
	}

}
