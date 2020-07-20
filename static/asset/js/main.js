function plus_animate(id, input, icon, desc) {
    $(`#${id}`).on("click", function(){
        if($(`${input}`).is(":checked")){
            $( `.${icon}`).addClass("plus-rotate")
            $( `.${desc}`).addClass("show_item")

        }else{
             $(`.${icon}`).removeClass("plus-rotate")
             $(`.${desc}`).removeClass("show_item")
        }
        
    })
}


$( ".stylish_underscore" ).each(function( index, element ) {
    $(this).attr('class', `stylish_underscore_${index}`)
    
})


$( ".card" ).each(function( index, element ) {
    $(this).addClass(`card_${index}`)
    $(document).on({
        mouseenter:function(){
            $( `.stylish_underscore_${index}` ).addClass("show_item").addClass("stylish_underscore_nth")
        },
        mouseleave:function(){
            $( `.stylish_underscore_${index}` ).removeClass("show_item").removeClass("stylish_underscore_nth")
        }}, `.card_${index}`
      )

})


function main_toggler(btn_cls, div_cls){
    $(`.${btn_cls}`).on("click", function(){
        $( `.${div_cls}` ).toggle();
        if($( `.${div_cls}` ).is(":visible")){
           $( `.${btn_cls}` ).html( "Show Less" );
        }else{
           $( `.${btn_cls}` ).html( "Show More" );
        }   

    });
}

plus_animate("main_projects__item_1", "input[name='main_projects__item_1-checkbox']", "plus-1", "main_projects__item_1__desc")
plus_animate("main_projects__item_2", "input[name='main_projects__item_2-checkbox']", "plus-2", "main_projects__item_2__desc")
plus_animate("main_projects__item_3", "input[name='main_projects__item_3-checkbox']", "plus-3", "main_projects__item_3__desc")
plus_animate("main_projects__item_4", "input[name='main_projects__item_4-checkbox']", "plus-4", "main_projects__item_4__desc")
main_toggler("show_more-btn", "toggler")
main_toggler("show_more-stack-btn", "stack_toggler")


