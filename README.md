# Experimental
Experimental programs repository.

# ExperimentalRoom4.html
実験室側のモニター画面。任意の文字列をID名にする（ただし半角英数字のみ）。ローカルでも録画が可能。ローカルで録画は「録画停止」ボタンがおされるまで録画が続く。ただし、ファイルは設定した時間（分）で文革保存される。

# MonitorRoom4.hmtl
監視室側のモニター画面。

# ImageMonitor.html
2023年度AI監視員実験用のAI監視員。カメラ映像内の指定エリア内に赤、青、白のエリアが一定以上存在した場合に、それぞれの色に対応したVoiceを流す。
VoiceはImageMonitor内に格納されている音声ファイル。

# CalcQuiz.html
2023年度AI監視員実験用のタスク用計算ツール。2桁×1桁の暗算課題で、解答の正解不正解とそれぞれの問題が提示されてから回答が入力されるまでの時間を計測する。
実際にはGoogle Apps Scriptに実装されており、そちらでは問題はGoogle Drive上のスプレッドシートに掲載されている。また回答ログもGoogle Drive上に保存される。

