package maker0921��������;

public class B01Circle {
	
	//����Բ�İ뾶
	int mr;
	//����Բ�� ��x������
	int x;
	//����Բ��y�������
	int y;
	
	//Բ��
	B01Point p=new B01Point();
	
	//����Բ�İ뾶
	void setR(int r) {
		mr=r;
	}
	//��ȡԲ�İ뾶
	int getR() {
		return mr;
	}
	//����Բ�ĵ�x������
	void setMx(int x1) {
		x=x1;
		
	}
	
	//��ȡԲ�ĵ�x������
	int getMx() {
			return x;
	}
		
	
	//����Բ�ĵ�y�������
	void setMy(int y1) {
			y=y1;
			
	}
	
	
	//��ȡԲ�ĵ�y�������
	int getMy() {
			return y;
	}
		
	
	//����Բ�� 
	void setH(B01Point p1) {
		p=p1;
	}
	
	//��ȡԲ��
	B01Point getH() {
		return p;
	}
	
	
	//�жϵ���Բ֮��Ĺ�ϵ
//	void pd(B01Point a) {
//		
//		//��ȡ����Բ�ĵ�ľ����ƽ��
//		int ab=(a.mx-x)*(a.mx-x)+(a.my-y)*(a.my-y);
//	
//		
//		//��ȡԲ�İ뾶��ƽ��
//		int rr=mr*mr;
//		
//		if(ab>rr) {
//			System.out.println("����Բ��");
//		}else if(ab<rr) {
//			System.out.println("����Բ��");
//		}else if(ab==rr) {
//			System.out.println("����Բ��");
//		}
//	}
	
	//�жϵ���Բ֮��Ĺ�ϵ
	void pd(B01Point a) {
			
	//��ȡ����Բ�ĵ�ľ����ƽ��
	  int ab=(a.mx-p.mx)*(a.mx-p.mx)+(a.my-p.my)*(a.my-p.my);
		
			
	  //��ȡԲ�İ뾶��ƽ��
	  int rr=mr*mr;
			
	  if(ab>rr) {
			System.out.println("����Բ��");
	  }else if(ab<rr) {
			System.out.println("����Բ��");
	  }else if(ab==rr) {
			System.out.println("����Բ��");
	  }
	  
     }
	
	
	
	
	
	

}
