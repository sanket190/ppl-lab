
;; Function f (f, funcdef_no=0, decl_uid=1908, cgraph_uid=1, symbol_order=1)

f ()
{
  int c;
  int b;
  int a;

  a = Z;
  if (a <= 9) goto <D.1914>; else goto <D.1915>;
  <D.1914>:
  b = 5;
  c = 17;
  goto <D.1916>;
  <D.1915>:
  b = 6;
  c = 20;
  if (a == 0) goto <D.1917>; else goto <D.1918>;
  <D.1917>:
  c = 0;
  <D.1918>:
  <D.1916>:
  _1 = b * 10;
  _2 = c + _1;
  Z = _2;
  return;
}


