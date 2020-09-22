package maker0921代码重敲;

public class B01Circle {
	
	//定义圆的半径
	int mr;
	//定义圆心 的x轴坐标
	int x;
	//定义圆的y轴的坐标
	int y;
	
	//圆心
	B01Point p=new B01Point();
	
	//设置圆的半径
	void setR(int r) {
		mr=r;
	}
	//获取圆的半径
	int getR() {
		return mr;
	}
	//设置圆心的x轴坐标
	void setMx(int x1) {
		x=x1;
		
	}
	
	//获取圆心的x轴坐标
	int getMx() {
			return x;
	}
		
	
	//设置圆心的y轴的坐标
	void setMy(int y1) {
			y=y1;
			
	}
	
	
	//获取圆心的y轴的坐标
	int getMy() {
			return y;
	}
		
	
	//设置圆心 
	void setH(B01Point p1) {
		p=p1;
	}
	
	//获取圆心
	B01Point getH() {
		return p;
	}
	
	
	//判断点与圆之间的关系
//	void pd(B01Point a) {
//		
//		//获取点与圆心点的距离的平方
//		int ab=(a.mx-x)*(a.mx-x)+(a.my-y)*(a.my-y);
//	
//		
//		//获取圆的半径的平方
//		int rr=mr*mr;
//		
//		if(ab>rr) {
//			System.out.println("点在圆外");
//		}else if(ab<rr) {
//			System.out.println("点在圆内");
//		}else if(ab==rr) {
//			System.out.println("点在圆上");
//		}
//	}
	
	//判断点与圆之间的关系
	void pd(B01Point a) {
			
	//获取点与圆心点的距离的平方
	  int ab=(a.mx-p.mx)*(a.mx-p.mx)+(a.my-p.my)*(a.my-p.my);
		
			
	  //获取圆的半径的平方
	  int rr=mr*mr;
			
	  if(ab>rr) {
			System.out.println("点在圆外");
	  }else if(ab<rr) {
			System.out.println("点在圆内");
	  }else if(ab==rr) {
			System.out.println("点在圆上");
	  }
	  
     }
	
	
	
	
	
	

}
