def my_test ( arg1 , *args , **kwargs ):
    print ( arg1, args , kwargs )

    param1 = args[0]
    print ( param1 )
    
    kwparam1 = kwargs.get('id')
    print ( kwparam1 )



my_test( 'request', '1', '2', '3' ,id='test' , oms='oms' )    
   