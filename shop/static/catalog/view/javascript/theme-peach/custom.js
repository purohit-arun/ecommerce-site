/* responsive menu */
function openNav() {
    $('body').addClass("active");
    document.getElementById("mySidenav").style.width = "280px";
}
function closeNav() {
    $('body').removeClass("active");
    document.getElementById("mySidenav").style.width = "0";
}

 /* loader */
$(window).load(function myFunction() {
  $(".s-panel .loader").removeClass("wrloader");
});

//go to top
$(document).ready(function () {
    $("#common-home").parent().addClass("home-page");
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('#scroll').fadeIn();
        } else {
            $('#scroll').fadeOut();
        }
    });
    $('#scroll').click(function () {
        $("html, body").animate({scrollTop: 0}, 600);
        return false;
    });
});


$(document).ready(function () {
    if ($(window).width() <= 991) {
        $('.menusp').appendTo('.appmenu');
        $('.curr').appendTo('.haccount');
        $('.langg').appendTo('.haccount');
    }

    $('.toprightw .owl-carousel.owl-theme .owl-buttons').appendTo('.apponbtn');
});


// function openSearch() {
//     $('body').addClass("active-search");
//     document.getElementById("search").style.height = "auto";
//     $('#search').addClass("sideb");
//     // $('.search_query').attr('autofocus', 'autofocus').focus();
// }
// function closeSearch() {
//     $('body').removeClass("active-search");
//     document.getElementById("search").style.height = "0";
//     $('#search').addClass("siden");
//     // $('.search_query').attr('autofocus', 'autofocus').focus();
// }


$(document).ready(function () {
$("#ratep,#ratecount").click(function() {
    $('body,html').animate({
        scrollTop: $(".product-tab").offset().top 
    }, 1500);
});
});

/* dropdown effect of account */
$(document).ready(function () {
    if ($(window).width() <= 767) {
    $('.catfilter').appendTo('.appres');

    $('.dropdown a.account').on("click", function(e) {
        $(this).next('ul').toggle();
        e.stopPropagation();
        e.preventDefault();
    });
}
$('.martbtes').appendTo('.test-dec');
// $('.imgleft').appendTo('.imgleftspe');
});

$(document).ready(function () {
$('.dropdown button.test').on("click", function(e)  {
    $(this).next('ul').toggle();
    e.stopPropagation();
    e.preventDefault();
});
});



/* dropdown */

/* sticky header */
  if ($(window).width() >= 992) {
 $(document).ready(function(){
      $(window).scroll(function () {
        if ($(this).scrollTop() > 700) {
            $('.homemenu').addClass('fixed fadeInDown animated');
        } else {
            $('.homemenu').removeClass('fixed fadeInDown animated');
        }
      });
});
};

$(document).ready(function(){
if ($(document).width() >= 1410){
     var count_block = $('.site-nav .moremenu').length;
     var number_blocks = 11;
     if(count_block < number_blocks){
          return false; 
     } else {
          
          $('.site-nav .moremenu').each(function(i,n){
                if(i == number_blocks) {
                     $('.site-nav').append('<li class="view_more"><a class="dropdown-item"><i class="fa fa-plus"></i> More</a></li>');
                }
                if(i> number_blocks) {
                     $(this).addClass('wr_hide_menu');
                }
          })
          $('.wr_hide_menu').hide();
          $('.view_more').click(function() {
                $(this).toggleClass('active');
                $('.wr_hide_menu').slideToggle();
          });
     }
}
});

$(document).ready(function(){
if (($(document).width() >= 1200) && ($(document).width() <= 1409)){
     var count_block = $('.site-nav .moremenu').length;
     var number_blocks = 7;
     if(count_block < number_blocks){
          return false; 
     } else {
          
          $('.site-nav .moremenu').each(function(i,n){
                if(i == number_blocks) {
                     $('.site-nav').append('<li class="view_more"><a class="dropdown-item"><i class="fa fa-plus"></i> More</a></li>');
                }
                if(i> number_blocks) {
                     $(this).addClass('wr_hide_menu');
                }
          })
          $('.wr_hide_menu').hide();
          $('.view_more').click(function() {
                $(this).toggleClass('active');
                $('.wr_hide_menu').slideToggle();
          });
     }
}
});

$(document).ready(function(){
if (($(document).width() >= 992) && ($(document).width() <= 1199)){
     var count_block = $('.site-nav .moremenu').length;
     var number_blocks = 5;
     if(count_block < number_blocks){
          return false; 
     } else {
          
          $('.site-nav .moremenu').each(function(i,n){
                if(i == number_blocks) {
                     $('.site-nav').append('<li class="view_more"><a class="dropdown-item"><i class="fa fa-plus"></i> More</a></li>');
                }
                if(i> number_blocks) {
                     $(this).addClass('wr_hide_menu');
                }
          })
          $('.wr_hide_menu').hide();
          $('.view_more').click(function() {
                $(this).toggleClass('active');
                $('.wr_hide_menu').slideToggle();
          });
     }
}
});

$(document).ready(function(){
if (($(document).width() >= 768) && ($(document).width() <= 991)){
     var count_block = $('.site-nav .moremenu').length;
     var number_blocks = 3;
     if(count_block < number_blocks){
          return false; 
     } else {
          
          $('.site-nav .moremenu').each(function(i,n){
                if(i == number_blocks) {
                     $('.site-nav').append('<li class="view_more"><a class="dropdown-item"><i class="fa fa-plus"></i> More</a></li>');
                }
                if(i> number_blocks) {
                     $(this).addClass('wr_hide_menu');
                }
          })
          $('.wr_hide_menu').hide();
          $('.view_more').click(function() {
                $(this).toggleClass('active');
                $('.wr_hide_menu').slideToggle();
          });
     }
}
});

$(document).ready(function(){

    $('.img-thumb').click(function () {

     var src = $(this).attr('src');
     console.log($(this).closest(".product-thumb").find('.js-product-cover').attr('src',src));
});
});