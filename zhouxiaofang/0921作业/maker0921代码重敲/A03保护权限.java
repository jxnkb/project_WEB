package maker0921��������;

import maker.BB02Son;
import maker.BB02����;
import maker0921��������.BM04;

public class A03����Ȩ�� {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������

		//1.���ñ��ļ��ı�����Ա
		test();
		System.out.println(a);
		
		//2.���ñ����������ļ�������ı�����Ա
		B02���� m=new B02����();
		m.test02();
		System.out.println(m.b);
		
		//3.������һ�����е�����ı�����Ա		
		BB02���� m2=new BB02����();
		
		//����ֱ�ӷ�����һ��������ı�����Ա
		//m2.test03(); 
		//System.out.println(m2.myb);
		  //1.���Ǹ����б�����Ա������,����һ�����з���,���Լ�ӵĵ��ø���Ĺ��г�Ա�����ñ�����Ա
		m2.test003();
		System.out.println(m2.getMyb());
//		  //2.����һ������,����̳е�����һ�����к��б�����Ա,Ȼ���ڸ�������дһ�����ñ�����Ա�Ĺ��з���,
//		      //���ڱ��ļ����ø�����Ĺ��з���
		   BB02Son m3=new BB02Son();
		   m3.test022();
		   
		//4.�������һ������,����̳е�����һ�����к��б�����Ա,Ȼ���ڸ�������дһ�����ñ�����Ա�Ĺ��з���,
		 //���ڱ��ļ����ø�����Ĺ��з���
		   BM04 m4=new BM04();
		   m4.BMtest();
	}
	
	protected static void test() {
		System.out.println("�����б���Ȩ�޵�test");
	
	}
	
	protected static int a=10;

}
