(function($){
	'use strict';

	// 找出所有信件內容中的 HTML
	function findallReplacedKeywordSymbol(mail_html_str){
		// g 表示全局去找，做多次比對
		// 該比對的格式中 {{ var }} 中與大括弧要有空白
		var pattern = /{{ [\u4e00-\u9fa5_a-zA-Z]+ }}/g;
		var matched = mail_html_str.match(pattern);
		console.log("比對到的有：", matched);
		return matched;
	};
	
	$('#subject-text').on('change', function(){
		var mail_subject = $(this).val();
		console.log('信件主旨：' + mail_subject);
	});

	// 偵測信件內容的 div 中有變更時的事件
	$('#contentarea').bind('DOMSubtreeModified', function(event) {
		console.log('Content Modified! Current content:' + '\n\n' + this.innerHTML);
		var matched = findallReplacedKeywordSymbol(this.innerHTML);
		if (matched != null){
			console.log(matched);
			// 準備好的 html 樣式
			$.get('/template/mail/keypair').success(function(data) {
				// 讀取 html 檔案並且把匹配到的資料方上去
				var matched_node = $(data);
				console.log(matched_node.html());
				matched_node.find('#mail-keypair').append('<tr><th>' + matched.join('</th></tr><tr><th>') + '</th><tr>');
				console.log(matched_node.html());
				$('#replace-keys').html(matched_node.html());
				console.log($('#replace-keys').html());
				
 			});
			var matched_html = '';
			// $('#replace-keys').html(

			// );
		}
		
	});
	
	// $('#file-dropzone').dropzone({
	// 	'dictDefaultMessage': '上傳你的檔案'
	// });

	// "fileDropzone" is the camelized(駝峰命名) version of the HTML element's ID file-dropzone
	Dropzone.options.fileDropzone = {
	paramName: "file", // The name that will be used to transfer the file
	dictDefaultMessage:  '上傳你的檔案',
	maxFilesize: 2, // MB
	uploadMultiple: false,
	accept: function(file, done) {
	  if (file.name == "justinbieber.jpg") {
		done("Naha, you don't.");
	  }
	  else { done(); }
	}
  };
})(jQuery);