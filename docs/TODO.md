1. 在`slidev-math-videos`项目建一个前端网站，部署到GitHub Pages，专门展示manim视频和配套的介绍文档和代码。网站颜色主题和TPM项目一致（所以还需要先把TPM项目的CSS变量整理成标准shadcn的样子），存储服务暂定阿里云OSS
2. 把相关特性引入TPM项目
3. 以前发布过的技术博客都可以考虑制作视频。不局限于manim，也可以是slidev
4. 新视频灵感：把圆锥和抛物体扔进水箱，画出函数关系图
5. `manim_schema\json_driven_scene.py`对齐视频的技术方案：srt新增注释，表示对应哪个vgroup，单个vgroup新增标识属性供匹配。解析srt，拿到每一个`self.play`调用的`run_time`
6. `show_title`和`show_ending`的时间等参数需要动态化
