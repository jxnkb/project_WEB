package test3;
import java.util.Scanner;
public class A11switch {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
    int a=2;
    switch(a) {
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
    	 break;
    }
    boolean b=true;
    float f=20.22f;
    double d=20.22;
    switch (a) {
//    1.()����Ҫ�����ֱ����򷵻صĽ�������ֵı��ʽ
	case 20://2.case ��������ǳ������ʽ
		System.out.println("a>10 && a<20");
		break;
	
	default:
		break;
	}
    	  
//	����:�����������ͱ���,Ȼ��ӿ���̨��ȡһ���ַ�,�����+��ô���������������,����ʲô���žͶ�Ӧ����ʲô
//	//�ӿ���̨��ȡһ���ַ�
//    char d=Scan.next().charAt(0);
    int a1=10;
    int b1=20;
    Scanner scanner=new Scanner(System.in);
    char d1=scanner.next().charAt(0);
//	System.out.println(d1);
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
		System.out.println("������ķ��Ų���ȷ");
		break;
	}
        
        
    }
		
	}


