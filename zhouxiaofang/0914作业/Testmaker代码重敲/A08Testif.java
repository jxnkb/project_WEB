package Testmaker��������;

import java.util.Scanner;

public class A08Testif {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������

//		int a=10;
	//	if(a) { //������ǲ������͵ı���
			
//			System.out.println("����if��������");
//		}
		
		
		boolean b=true;
		if(b) {
			
			System.out.println("����if��������");
		}
		
		
		int a1=30;
		int b1=20;
		if(a1>b1) {
			System.out.println("����a1>b1��������");
		}
		
		if(100>20) {
			System.out.println("����100>20��������");
		}
		
//		����:�ӿ���̨����һ������,�ñ���a����,�������������10,�ʹ�ӡ"��������ݴ���10"	
		
		Scanner scan=new Scanner(System.in);
		int a2=scan.nextInt();
		if(a2>10) {
			System.out.println("��������ݴ���10");
		}
		
			
		
	}

}
