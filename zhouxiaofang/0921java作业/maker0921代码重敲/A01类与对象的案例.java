package maker0921��������;

public class A01�������İ��� {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
		//��������
		B01Point aa=new B01Point();
		aa.setX(10);
		aa.setY(20);
		
		//����Բ����
		B01Circle bb=new B01Circle();
//		bb.setMx(20);
//		bb.setMy(30);
//		bb.setR(5);
//		
//		bb.pd(aa);
		
		
		//����Բ��
		B01Point p1=new B01Point();//p1(xx3,xx3);
		//�ѵ㸳ֵ��Բ��
		bb.setH(p1);
		
		bb.pd(aa);

	}

}
