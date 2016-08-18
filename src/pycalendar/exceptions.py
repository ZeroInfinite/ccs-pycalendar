##
#    Copyright (c) 2011-2013 Cyrus Daboo. All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
##

class ErrorBase(Exception):

    def __init__(self, reason, data=""):
        self.mReason = reason
        self.mData = data


    def __str__(self):
        return "{}: {}".format(self.mReason, self.mData) if self.mData else self.mReason



class InvalidData(ErrorBase):
    pass



class InvalidComponent(ErrorBase):
    pass



class InvalidProperty(ErrorBase):
    pass



class ValidationError(ErrorBase):
    pass



class NoTimezoneInDatabase(Exception):

    def __init__(self, dbpath, tzid):
        self.mTZDBpath = dbpath
        self.mTZID = tzid
