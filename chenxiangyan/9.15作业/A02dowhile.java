package maker2;

public class A02dowhile {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		int a=0;
		do {
			System.out.println(a);
			a++;
			
		}while(a<10);//注意这里有分号
		System.out.println("--------------");
//		案例:输出1-100的单数
		int b=0;
		do {
			
			if(b%2==1) {
				System.out.println(b);
			}
			b++;
		}while(b<=100);
		
		System.out.println("------------");
//		案例:使用while嵌套循环打印如下图形
//		*
//		* *
//		* * *
//		* * * *
//		* * * * *
		/*
		 * int i=0;
			#外循环
		while (i<5){
    		int j=0
    		#内循环
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
