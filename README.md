# pisensor(調整中)
RaspberryPiで使用されるセンサー向けのPython package。
本パッケージはGPIO・I2C・SPIというRaspberryPiで使用できるI/Fと、センサの駆動方式に着目しクラス階層を設計する。
以下に設計した各インタフェース・クラスの目的と簡単な説明を示す。

## インタフェース・抽象クラス

 - gpio_sensor_conf.py
 GPIOセンサを定義するためのインタフェース
 GPIOのPIN番号を保持する。

 - smbus_sensor_conf.py
 I2Cセンサを定義するためのインタフェース。
 I2Cセンサに割り当てられるアドレスを保持するように設計。

- spi_sensorconf.py
 SPIセンサを定義するためのインタフェース。
 使用するCEPINアドレスを保持し、コネクションを確立する。

 - event_driven_io.py
 イベント駆動センサを定義するインタフェース。本インタフェースを継承して定義するセンサクラスは、イベントとハンドラの追加・削除・呼び出しが行えるように実装する。

 - periodic_io.py
 周期駆動センサを定義するインタフェース。
 本インタフェースを継承して定義するセンサクラスは、センシングメソッドが各センサごとに異なるため、与えられたセンシングメソッドを周期的に実行するよう実装する。

 - demand_driven_io.py
 デマンド駆動センサを定義するインタフェース。
 本インタフェースを継承したセンサクラスでは、デマンドの実行とセンシングを行うよう実装する。

## 共通クラス
 - event_handler.py
センサクラスにイベントハンドラ機構を実装する。

 - demand.py
 デマンド駆動センサにおける、GPIO・I2C・SPIの各I/Fごとにデマンドを分類するためのクラス。

 - exception_method.py
 各センサクラスに例外処理を持たせる。例外処理は各センサで実装。GPIO・I2C・SPIの各I/Fごとに例外処理をある程度分けることができる。そのため、gpio_exception_methodのように例外処理を作成したほうが良いと思われる。

## センサクラス
各センサクラスはイベントハンドラ機構・例外処理を持つ。各IFと各駆動方式ごとにセンサが存在すると考えたため、計9つのセンサクラスを定義した。

 - event_gpio_sensor.py
 イベント駆動・GPIOを用いるセンサを想定したセンサ。
 既存モジュールを用い、イベント検知・ハンドラの呼び出しを実装。

 - event_smbus_sensor.py
 イベント駆動・I2Cセンサでは、周期的に特定のレジスタの値をセンシングを行う。センシング結果が、登録されたイベントと同じである場合登録されているハンドラを呼び出すように実装した。

 - event_spi_sensor.py
 イベント駆動I2Cセンサとほぼ同様に設計する。

 - periodic_gpio_sensor.py
 周期的にセンシングメソッドを実装した。また、周期の間隔・周期実行フラグに対するsetメソッドを持つ。

 - periodic_smbus_sensor.py
 同様に設計する。

 - periodic_spi_sensor.py
 同様に設計する。

 - demand_gpio_sensor.py
 デマンド駆動GPIOセンサでは、デマンドとして信号の立ち上と立ち下げがデマンドとして実行される場合があるため、各デマンドが実行できるように場合分けを行い実装した。
 詳しくはdemand.pyを参照。
 
 - demand_smbus_sensor.py
 I2Cセンサにおけるデマンドとして、特定のレジスタに対して特定の値を書き込みが行われる。そのため、本センサでは書き込みとセンシングメソッドを受け取り、書き込みの実行・センシングの順に行えるよう実装する。

 - demand_spi_sensor.py
I2Cセンサと同様に実装する。


## 課題
本パッケージはまだ調整中である。I2C・SPI用センサーはまだデバック中。
また、型判定などがしっかりと実装されていない。
