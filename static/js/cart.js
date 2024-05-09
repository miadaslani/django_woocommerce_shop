$('.addToCartBtn').click(function (e){
    e.preventDefault();

    let product_id = $(this).closest('.card_area').find('.prod_id').val();
    console.log('product_id',product_id)
    let token = $('input{name=csrfmiddlewaretoken').val();
    console.log('token',token)

    $.ajax({
        method:"POST",
        url: "/shop/add_to_cart/",
        data: {
            'product_id': product_id,
            csrfmiddlewaretoken: token
        },
        dataType:"dataType",
        success: function(responce){
            console.log(responce);
            // location.reload();
        }
    })
});