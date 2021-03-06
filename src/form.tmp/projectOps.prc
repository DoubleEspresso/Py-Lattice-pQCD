#procedure projectOps()

* // =========================================================
* // this file contains the replacement rules for the 
* // desired operator structure.  We find the coefficient
* // of this structure only.
* //
* // ---------------------------------------------------------

* // the quark wave function renormalization
* id sum(dum1?)*p(dum1?)*g(dum1?) = sf*OP;

* // the gluon wave function renormalization

* // the quark angular momentum operator
* id g(1)*p(2) = sf*OP;
* id g(2)*p(1) = sf*OP;

* // the quark angular momentum operator when computing g->q
 id sum(dum1?) * sum(dum2?) * g(dum1?)* q(dum1?) * p(dum2?) * q(dum2?) = sf * OP;

* // the gluon angular momentum operator
* // there may be an overall sign on the 1/2 here.
*id sum(dum1?)*p(dum1?)^2*q(1)*q(2) = 1/2*sf*OP;

* // after re-interpreting the external indices, we mix into a G operator with this structure:
*id sum(dum1?)*sum(dum2?)*p(dum1?)*p(dum2?)*q(dum1?)*q(dum2?) = 1/2*sf*OP;
id q(dum1?)^2 = 0;

id sf^pw1?!{-20,1} = 0;
id sf = 1;


* // ---------------------------------------------------------
* // set rw and rho here
* // note that when integrating, rw
* // and rho need to be set in mathematica codes.
* //
* // id rw = 1;


* //-----------------------------------------------------------
* // any remaining sums are replaced by the dimension DIM
* // in all dim-reg calculations.

* // remove delta fncs of external indices (assume ex1 != ex2)
repeat;
  id d(1,2) = 0; id d(1,3) = 0; id d(1,4) = 0;
  id d(2,1) = 0; id d(2,3) = 0; id d(2,4) = 0;
  id d(3,1) = 0; id d(3,2) = 0; id d(3,4) = 0;
  id d(4,1) = 0; id d(4,2) = 0; id d(4,3) = 0;
  id d(1,1) = 1; id d(2,2) = 1; id d(3,3) = 1;
  id d(4,4) = 1;
endrepeat;

* // replace any left-over summations with the dimension
id sum(dum1?) = DIM;
