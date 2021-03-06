#procedure diracSimplify()


* // simplifies long products of gamma matrices through direct replacements.
* // These replacements have been pre-computed using FeynCalc in D-dimensions.
*==========================================================================
* //
* //  make reps for gamma matrices
* //
*//repeat;
  id G(dum1?)*G(dum2?)*G(dum3?)*G(dum4?)*G(dum5?)*G(dum6?)*G(dum7?)*G(dum8?) = G(dum1,dum2,dum3,dum4,dum5,dum6,dum7,dum8);
  id G(dum1?)*G(dum2?)*G(dum3?)*G(dum4?)*G(dum5?)*G(dum6?)*G(dum7?) = G(dum1,dum2,dum3,dum4,dum5,dum6,dum7);
  id G(dum1?)*G(dum2?)*G(dum3?)*G(dum4?)*G(dum5?)*G(dum6?) = G(dum1,dum2,dum3,dum4,dum5,dum6);
  id G(dum1?)*G(dum2?)*G(dum3?)*G(dum4?)*G(dum5?) = G(dum1,dum2,dum3,dum4,dum5);
  id G(dum1?)*G(dum2?)*G(dum3?)*G(dum4?) = G(dum1,dum2,dum3,dum4);
  id G(dum1?)*G(dum2?)*G(dum3?) = G(dum1,dum2,dum3);
  id G(dum1?)*G(dum2?) = G(dum1,dum2);
*//endrepeat;

** ORDER SIX REPS ** 
id G(dum1?,dum2?,dum3?,dum4?,dum5?,dum6?) = 
   ld(dum1,dum2)*ld(dum3,dum4)*ld(dum5,dum6)-ld(dum1,dum2)*ld(dum3,dum5)*
   ld(dum4,dum6)+ld(dum1,dum2)*ld(dum3,dum6)*ld(dum4,dum5)-
   ld(dum1,dum3)*ld(dum2,dum4)*ld(dum5,dum6)+ld(dum1,dum3)*ld(dum2,dum5)*
   ld(dum4,dum6)-ld(dum1,dum3)*ld(dum2,dum6)*ld(dum4,dum5)+
   ld(dum1,dum4)*ld(dum2,dum3)*ld(dum5,dum6)-ld(dum1,dum4)*ld(dum2,dum5)*
   ld(dum3,dum6)+ld(dum1,dum4)*ld(dum2,dum6)*ld(dum3,dum5)-
   ld(dum1,dum5)*ld(dum2,dum3)*ld(dum4,dum6)+ld(dum1,dum5)*ld(dum2,dum4)*
   ld(dum3,dum6)-ld(dum1,dum5)*ld(dum2,dum6)*ld(dum3,dum4)+
   ld(dum1,dum6)*ld(dum2,dum3)*ld(dum4,dum5)-ld(dum1,dum6)*ld(dum2,dum4)*
   ld(dum3,dum5)+ld(dum1,dum6)*ld(dum2,dum5)*ld(dum3,dum4)+g(5)*eps(
   dum1,dum2,dum3,dum4)*ld(dum5,dum6)-g(5)*eps(dum1,dum2,dum3,dum5)*
   ld(dum4,dum6)+g(5)*eps(dum1,dum2,dum3,dum6)*ld(dum4,dum5)+g(5
   )*eps(dum1,dum4,dum5,dum6)*ld(dum2,dum3)-g(5)*eps(dum2,dum4,dum5,
   dum6)*ld(dum1,dum3)+g(5)*eps(dum3,dum4,dum5,dum6)*ld(dum1,dum2)-
   sig(dum1,dum2)*ld(dum3,dum4)*ld(dum5,dum6)*i_+sig(dum1,dum2)*
   ld(dum3,dum5)*ld(dum4,dum6)*i_-sig(dum1,dum2)*ld(dum3,dum6)*
   ld(dum4,dum5)*i_+sig(dum1,dum3)*ld(dum2,dum4)*ld(dum5,dum6)*i_-sig(
   dum1,dum3)*ld(dum2,dum5)*ld(dum4,dum6)*i_+sig(dum1,dum3)*ld(dum2,dum6)
   *ld(dum4,dum5)*i_-sig(dum1,dum4)*ld(dum2,dum3)*ld(dum5,dum6)*i_+sig(
   dum1,dum4)*ld(dum2,dum5)*ld(dum3,dum6)*i_-sig(dum1,dum4)*ld(dum2,dum6)
   *ld(dum3,dum5)*i_+sig(dum1,dum5)*ld(dum2,dum3)*ld(dum4,dum6)*i_-sig(
   dum1,dum5)*ld(dum2,dum4)*ld(dum3,dum6)*i_+sig(dum1,dum5)*ld(dum2,dum6)
   *ld(dum3,dum4)*i_-sig(dum1,dum6)*ld(dum2,dum3)*ld(dum4,dum5)*i_+sig(
   dum1,dum6)*ld(dum2,dum4)*ld(dum3,dum5)*i_-sig(dum1,dum6)*ld(dum2,dum5)
   *ld(dum3,dum4)*i_-sig(dum2,dum3)*ld(dum1,dum4)*ld(dum5,dum6)*i_+sig(
   dum2,dum3)*ld(dum1,dum5)*ld(dum4,dum6)*i_-sig(dum2,dum3)*ld(dum1,dum6)
   *ld(dum4,dum5)*i_+sig(dum2,dum4)*ld(dum1,dum3)*ld(dum5,dum6)*i_-sig(
   dum2,dum4)*ld(dum1,dum5)*ld(dum3,dum6)*i_+sig(dum2,dum4)*ld(dum1,dum6)
   *ld(dum3,dum5)*i_-sig(dum2,dum5)*ld(dum1,dum3)*ld(dum4,dum6)*i_+sig(
   dum2,dum5)*ld(dum1,dum4)*ld(dum3,dum6)*i_-sig(dum2,dum5)*ld(dum1,dum6)
   *ld(dum3,dum4)*i_+sig(dum2,dum6)*ld(dum1,dum3)*ld(dum4,dum5)*i_-sig(
   dum2,dum6)*ld(dum1,dum4)*ld(dum3,dum5)*i_+sig(dum2,dum6)*ld(dum1,dum5)
   *ld(dum3,dum4)*i_-sig(dum3,dum4)*ld(dum1,dum2)*ld(dum5,dum6)*i_+sig(
   dum3,dum4)*ld(dum1,dum5)*ld(dum2,dum6)*i_-sig(dum3,dum4)*ld(dum1,dum6)
   *ld(dum2,dum5)*i_+sig(dum3,dum5)*ld(dum1,dum2)*ld(dum4,dum6)*i_-sig(
   dum3,dum5)*ld(dum1,dum4)*ld(dum2,dum6)*i_+sig(dum3,dum5)*ld(dum1,dum6)
   *ld(dum2,dum4)*i_-sig(dum3,dum6)*ld(dum1,dum2)*ld(dum4,dum5)*i_+sig(
   dum3,dum6)*ld(dum1,dum4)*ld(dum2,dum5)*i_-sig(dum3,dum6)*ld(dum1,dum5)
   *ld(dum2,dum4)*i_-sig(dum4,dum5)*ld(dum1,dum2)*ld(dum3,dum6)*i_+sig(
   dum4,dum5)*ld(dum1,dum3)*ld(dum2,dum6)*i_-sig(dum4,dum5)*ld(dum1,dum6)
   *ld(dum2,dum3)*i_+sig(dum4,dum6)*ld(dum1,dum2)*ld(dum3,dum5)*i_-sig(
   dum4,dum6)*ld(dum1,dum3)*ld(dum2,dum5)*i_+sig(dum4,dum6)*ld(dum1,dum5)
   *ld(dum2,dum3)*i_-sig(dum5,dum6)*ld(dum1,dum2)*ld(dum3,dum4)*i_+sig(
   dum5,dum6)*ld(dum1,dum3)*ld(dum2,dum4)*i_-sig(dum5,dum6)*ld(dum1,dum4)
   *ld(dum2,dum3)*i_;

** ORDER FIVE REPS **
id G(dum1?,dum2?,dum3?,dum4?,dum5?) =
           -g(5,dum4)*eps(dum1,dum2,dum3,dum5)
	   +g(5,dum5)*eps(dum1,dum2,dum3,dum4)
	   +sum(tmp)*g(5,tmp)*eps(dum1,dum2,dum3,tmp)*ld(dum4,dum5)
	   +sum(tmp)*g(5,tmp)*eps(dum1,dum4,dum5,tmp)*ld(dum2,dum3)
	   -sum(tmp)*g(5,tmp)*eps(dum2,dum4,dum5,tmp)*ld(dum1,dum3)
	   +sum(tmp)*g(5,tmp)*eps(dum3,dum4,dum5,tmp)*ld(dum1,dum2)
	   +g(dum1)*ld(dum2,dum3)*ld(dum4,dum5)
	   -g(dum1)*ld(dum2,dum4)*ld(dum3,dum5)
	   +g(dum1)*ld(dum2,dum5)*ld(dum3,dum4)
	   -g(dum2)*ld(dum1,dum3)*ld(dum4,dum5)
	   +g(dum2)*ld(dum1,dum4)*ld(dum3,dum5)
	   -g(dum2)*ld(dum1,dum5)*ld(dum3,dum4)
	   +g(dum3)*ld(dum1,dum2)*ld(dum4,dum5)
	   -g(dum3)*ld(dum1,dum4)*ld(dum2,dum5)
	   +g(dum3)*ld(dum1,dum5)*ld(dum2,dum4)
	   -g(dum4)*ld(dum1,dum2)*ld(dum3,dum5)
	   +g(dum4)*ld(dum1,dum3)*ld(dum2,dum5)
	   -g(dum4)*ld(dum1,dum5)*ld(dum2,dum3)
	   +g(dum5)*ld(dum1,dum2)*ld(dum3,dum4)
	   -g(dum5)*ld(dum1,dum3)*ld(dum2,dum4)
	   +g(dum5)*ld(dum1,dum4)*ld(dum2,dum3);


** ORDER FOUR REPS **
id G(dum1?,dum2?,dum3?,dum4?) =   ld(dum1,dum2)*ld(dum3,dum4) 
			        - ld(dum1,dum3)*ld(dum2,dum4) 
			        + ld(dum1,dum4)*ld(dum2,dum3) 
			        + g(5)*eps(dum1,dum2,dum3,dum4) 
			        - sig(dum1,dum2)*ld(dum3,dum4)*i_
			        + sig(dum1,dum3)*ld(dum2,dum4)*i_ 
			        - sig(dum1,dum4)*ld(dum2,dum3)*i_ 
			        - sig(dum2,dum3)*ld(dum1,dum4)*i_ 
			        + sig(dum2,dum4)*ld(dum1,dum3)*i_ 
			        - sig(dum3,dum4)*ld(dum1,dum2)*i_;

** ORDER THREE REPS **
id G(dum1?,dum2?,dum3?)       =    sum(tmp)*g(5,tmp)*eps(dum1,dum2,dum3,tmp) 
                                 + g(dum1)*ld(dum2,dum3) 
			         - g(dum2)*ld(dum1,dum3) 
			         + g(dum3)*ld(dum1,dum2);

** ORDER TWO REPS **
id G(dum1?,dum2?) = ld(dum1,dum2) - sig(dum1,dum2)*i_;

*//
*// after these replacements, we make gamma a commuting function
*// so that the contract delta routines work properly
*//
id G(dum1?) = g(dum1);

*================================================================
* for un-polarized renormalization calculations, twist-2 operators
* etc. the sigma-tensor will vanish always, we make these replacements
* here.

*------------------------------
*/ reps for sig-tensor
*/ ensure that sig is anti-symmetric
*--------------------------------
id sig(dum1?,dum1?) = 0;
id sig(dum1?,dum2?)*p1?(dum1?)*p1?(dum2?) = 0;
id sig(dum1?,dum2?)*m?(dum1?)*m?(dum2?) = 0;
id sig(dum1?,dum2?)*s?(dum1?)*s?(dum2?) = 0;
id sig(dum1?,dum2?) = 0;

*--------------------
* FOR NOW SET EPS TO ZERO
*---------------------
id eps(dum1?,dum2?,dum3?,dum4?) = 0;


*---------------------------
* RESET THE ld(dum1?,dum2?)
*---------------------------
id ld(dum1?,dum2?) = d(dum1,dum2);