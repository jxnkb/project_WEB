package maker2��������;

import java.util.Scanner;

public class A09 {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
//		5��	�붨���һ�����Դ���8�����͵�����
			int[] arr5=new int[8];
			
		//	6��	����⣺����Ԫ�ز���(����ָ��Ԫ�ص�һ���������г��ֵ�����)
			Scanner scan=new Scanner(System.in);	
			int[] arr= {4,56,7,8,9};
			System.out.println("������Ҫ���ҵ�Ԫ��:");
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
