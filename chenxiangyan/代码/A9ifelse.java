package test3;
import java.util.Scanner;
public class A9ifelse {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
    int a=10;
    int b=20;
    if(a>b) {
    	System.out.println("a>b");
    }else {
    	System.out.println("a<=b");
    }
//    ����:�ӿ���̨������������,Ȼ���ӡ��������ֵ
    Scanner scanner=new Scanner(System.in);
    System.out.println("�������һ������");
    int a1=scanner.nextInt();
    System.out.println("������ڶ�������");
    int a2=scanner.nextInt();
    System.out.println("���������������");
    int a3=scanner.nextInt();
    
    if(a1>a2) {
    	if(a1>a3) {
    		System.out.println("a1���"+a1);
    	}else {
    		System.out.println("a3���"+a3);
    	}
    }else {
    	if(a2>a3) {
    		System.out.println("a2���"+a2);
    	}else {
    		System.out.println("a3���"+a3);
    	}
    }
    }
    
	}


