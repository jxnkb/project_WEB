package maker2��������;

public class A02dowhile {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
		int a=0;
		do {
			System.out.println(a);
			a++;
		}while(a<10); //ע�������зֺ�
		
//		����:���1-100�ĵ���
		int b=1;
		do {
			if(b%2==1) {
				System.out.println(b);
			}
			
			b+=1;
			
		}while(b<=100);
		
//		����:ʹ��whileǶ��ѭ����ӡ����ͼ��
//		*
//		* *
//		* * *
//		* * * *
//		* * * * *
		
		int i=0;
		while(i<5) {
			int j=0;
			while(j<i) {
				System.out.print("*");
				j++;
			}
			
			i++;
			System.out.println();
		}
		
		
		
		
		
		
		

	}

}
