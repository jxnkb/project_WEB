package maker2代码重敲;

import java.util.Scanner;

public class A09 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
//		5．	请定义出一个可以储存8个整型的数组
			int[] arr5=new int[8];
			
		//	6．	编程题：数组元素查找(查找指定元素第一次在数组中出现的索引)
			Scanner scan=new Scanner(System.in);	
			int[] arr= {4,56,7,8,9};
			System.out.println("请输入要查找的元素:");
			int num=scan.nextInt();
		//	System.out.println(num);
			for(int x=0;x<arr.length;x++) {
				
				if(arr[x]==num) {
					System.out.println(x);
				}
				x+=1;
			}
		
		
		
		
		
		
		

	}

}
