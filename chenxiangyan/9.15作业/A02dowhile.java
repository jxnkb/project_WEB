package maker2;

public class A02dowhile {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		int a=0;
		do {
			System.out.println(a);
			a++;
			
		}while(a<10);//ע�������зֺ�
		System.out.println("--------------");
//		����:���1-100�ĵ���
		int b=0;
		do {
			
			if(b%2==1) {
				System.out.println(b);
			}
			b++;
		}while(b<=100);
		
		System.out.println("------------");
//		����:ʹ��whileǶ��ѭ����ӡ����ͼ��
//		*
//		* *
//		* * *
//		* * * *
//		* * * * *
		/*
		 * int i=0;
			#��ѭ��
		while (i<5){
    		int j=0
    		#��ѭ��
    		while (j<=i){
        		System.out.print('*');
        		j=j+1
        	}

    		i=i+1
    		System.out.println();
    	}
		 */
		int i=0;
		while(i<5) {//i==2
			int j=0;
			while(j<=i) {//j==
				System.out.print('*');
				j+=1;
			}
			i+=1;
			System.out.println();
		}
		
	}
	

	


}
