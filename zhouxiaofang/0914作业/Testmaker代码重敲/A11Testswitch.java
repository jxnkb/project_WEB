package Testmaker��������;

import java.util.Scanner;

public class A11Testswitch {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
		int a=2;
		switch (a) {
		case 1:
		   System.out.println("1");
		   break;
		case 2:
		   System.out.println("2");
		   break;  
		case 3:
		   System.out.println("3");
		   break;  
		default:
		   System.out.println("����");
		   break;
		  
		}
	
		
		char c='a';
		switch (c) {
		case 'a':
			System.out.println("a");
		    break;
		case 'b':
			System.out.println("b");
		    break;
		case 'c':
			System.out.println("c");
		    break;	
		default:
			break;
			
		}
		
		boolean b=true;
		float f=20.33f;
		double d=20.44;
		switch (a) { //1.()����Ҫ�����ֱ����򷵻صĽ�������ֵı��ʽ
		case 20:  //2.case ��������ǳ������ʽ
			System.out.println("a>10 && a<20");
		    break;
		default:
		    break;
		
		}

//		����:�����������ͱ���,Ȼ��ӿ���̨��ȡһ���ַ�,�����+��ô���������������,����ʲô���žͶ�Ӧ����ʲô
//		//�ӿ���̨��ȡһ���ַ�
//		char d=scan.next().charAt(0);
		int a1=10;
		int b1=20;
		Scanner scan=new Scanner(System.in);
		char d1=scan.next().charAt(0);
		System.out.println(d1);
		switch (d1) {
		case '+':
			System.out.println(a1+b1);
		    break;
		case '-':
			System.out.println(a1-b1);
		    break;
		case '*':
			System.out.println(a1*b1);
		    break;		    
		case '/':
			System.out.println(a1/b1);
		    break;
		    	    
		default:
			System.out.println("��������");
			break;
		}
		
		
		
		
		
		
		
	}

}
