package zy922;
//1.����Ĵ�����дһ��
//2.���췽����˭���õ�
//ϵͳ
//3.����Ĺ��캯��Ĭ�ϵ��ø����ʲô���캯��
//�޲�
//4.�������Ĺ��캯��Ҫ���ø�����вι���,Ҫ��ʲô����
//super�ؼ���
//5.This��������ʲô
//���������ڵ�
//6.�̳еĹؼ�����ʲô
//extends
//7.�̳п��Լ̳и����˽�б�����?
//���ԣ�Ҫ��super


public class a1 {
	//8.дһ�������Ķ�̬����,���������Ǹ���,���������,������ӡ���������Ʒ��
	//��������
	public static class car{
		String brand;
		protected car(String brand){
			this.brand=brand;
		}
		void getbrand(){
			
		}
	}
	//��������1
	public static class BMW extends car{
		BMW(String brand) {
			super(brand);
			// TODO Auto-generated constructor stub
		}
		void getbrand(){
			System.out.println(brand);
		}
	}
	//��������2
	public static class Benz extends car{
		Benz(String brand) {
			super(brand);
			// TODO Auto-generated constructor stub
		}
		void getbrand(){
			System.out.println(brand);
		}
	}
	//��������3
	public static class Bentley extends car{
		Bentley(String brand) {
			super(brand);
			// TODO Auto-generated constructor stub
		}
		void getbrand(){
			System.out.println(brand);
		}
	}
	//��������
	static void printBrand(car a){
		a.getbrand();
	}
	
	
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//��������
		Benz b1=new Benz("����");
		Bentley b2=new Bentley("����");
		BMW b3=new BMW("����");
		//ִ�ж���
		printBrand(b1);
		printBrand(b2);
		printBrand(b3);
		
		
	}

}
