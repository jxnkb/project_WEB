package maker2��������;
import java.util.Random;

public class A06����� {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
		//��ʽһ
		for(int i=0;i<10;i++) {
			int a=(int)(Math.random()*100);
			System.out.println(a);
		}
		
		//��ʽ��
		Random r=new Random();
		for(int i=0;i<10;i++) {
			int a=r.nextInt(100);
			System.out.print(a+" ");
		}
		System.out.println("----------");
		
		//Math��ѧ��
		System.out.println(Math.pow(3, 2)); //ƽ��
		System.out.println(Math.sqrt(9));  //������
		System.out.println(Math.abs(-3));  //����ֵ
		

	}

}
