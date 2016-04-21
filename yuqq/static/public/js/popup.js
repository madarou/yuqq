jQuery(document).ready(function($) {
	$(".popup-bg").click(function() {
		$(".buybox").hide();
		$(this).hide();
	});
	$(".buy").click(function() {
		center($(".buybox"));
		$(".popup-bg").show();
		$(".buybox").show();
	});
	function center(obj) {
		var screenWidth = $(window).width(), screenHeight = $(window).height(); // 当前浏览器窗口的
		// 宽高
		var scrolltop = $(document).scrollTop();// 获取当前窗口距离页面顶部高度
		var objLeft = (screenWidth - obj.width()) / 2;
		var objTop = (screenHeight - obj.height()) / 2 + scrolltop;
		obj.css({
			left : (objLeft-30) + 'px',
			top : objTop + 'px',
			'display' : 'block'
		});
	}
});