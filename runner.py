import login
import createSchedule,logout
import unittest

# mysuite = unittest.TestSuite()
# mysuite.addTest(loginsucc.MyTestCase("testLogIn"))
# mysuite.addTest(loginsucc.MyTestCase("testLoginsucc"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))


# 执行登录
logincases = unittest.TestLoader().loadTestsFromTestCase(login.MyTestCase)
# 执行创建任务并调度
createSchedulecases = unittest.TestLoader().loadTestsFromTestCase(createSchedule.MyTestCase)
# 注销
logutcases = unittest.TestLoader().loadTestsFromTestCase(logout.MyTestCase)


mysuite = unittest.TestSuite([logincases, createSchedulecases, logutcases])

# mysuite.addTest(unittestdemo.MyTestCase("testLogIn"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))



myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)
