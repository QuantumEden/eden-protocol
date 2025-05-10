// /blockchain/contracts/meritcoin.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title MeritCoin
 * @dev Soulbound non-transferable XP-based token for the Eden Protocol
 *      Designed to represent symbolic growth and DAO participation integrity
 */

contract MeritCoin {
    address public admin;
    mapping(address => uint256) public xp;
    mapping(address => bool) public soulbound;

    event XPGranted(address indexed user, uint256 amount);
    event XPRevoked(address indexed user, uint256 amount);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    function grantXP(address user, uint256 amount) public onlyAdmin {
        require(user != address(0), "Invalid address");
        xp[user] += amount;
        soulbound[user] = true;
        emit XPGranted(user, amount);
    }

    function revokeXP(address user, uint256 amount) public onlyAdmin {
        require(xp[user] >= amount, "Insufficient XP to revoke");
        xp[user] -= amount;
        emit XPRevoked(user, amount);
    }

    function getXP(address user) public view returns (uint256) {
        return xp[user];
    }

    function isSoulbound(address user) public view returns (bool) {
        return soulbound[user];
    }

    // Prevent any kind of transfer or approval
    fallback() external payable {
        revert("This contract does not accept Ether");
    }
}
