package maker2��������;

public class A01while {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
//		int a=10;
	//	while(a) { //����,���ǲ�����
			
//		}
		
	//    boolean b=true;
	//    while(b) {
	    	
	//    }
	
	int a1=1;
	while (a1<=5) {
//		System.out.println(a1);	
		System.out.print(a1+" ");
		a1++;
	}
	
//	����:С��������ÿ�����2.5ԪǮ������������������ǣ�ÿ����һ���Ǵ�Ǯ�ĵ�5�����5�ı����Ļ���
//	�����Ứȥ6ԪǮ�����ʣ����������죬С���ſ��Դ浽100ԪǮ��
	/*
	 * 1.����洢Ǯ��������ӡ100,��ô������ѭ��
	 * 2.day%5==0  Ǯ-6
	 */
	//Ǯ
	double m=0;
	int day=0;
	while(m<=100) {
		m+=2.5;
		day+=1;
		if(day%5==0) {
			m=m-6;
		}
	}
	
	System.out.println(day);
	
	
	
		

	}

}
