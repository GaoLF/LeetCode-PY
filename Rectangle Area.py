#coding=utf-8
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    # 还是应该擅长找一个题目的规律
    # 这个题我第一次做的方法简直笨成猪，还要来回试所有的不同情况，稍有疏忽就错了
    # 求出两个矩形的重合部分，然后判断是否重合，如果重合，减去重合面积
    # 重合部分的求法就是两个左下求最大，两个右上求最小
    def computeArea(self, A, B, C, D, E, F, G, H):
        left,bottom = max(A,E),max(B,F)
        right,up = min(C,E),min(D,H)
        S  = (C-A)*(D-B) + (G-E)*(H-F)
        if right > left and up > bottom:
            S -= (right-left)*(up-bottom)
        return S

